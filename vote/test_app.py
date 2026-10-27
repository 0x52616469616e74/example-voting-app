import unittest

import app as vote_app


class FakeRedis:
    def __init__(self):
        self.items = []

    def rpush(self, queue, value):
        self.items.append((queue, value))


class VoteAppTests(unittest.TestCase):
    def setUp(self):
        self.client = vote_app.app.test_client()

    def test_health_endpoint(self):
        response = self.client.get('/healthz')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'status': 'ok'})

    def test_vote_is_queued(self):
        fake_redis = FakeRedis()
        original_get_redis = vote_app.get_redis
        vote_app.get_redis = lambda: fake_redis
        self.addCleanup(setattr, vote_app, 'get_redis', original_get_redis)

        response = self.client.post('/', data={'vote': 'a'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(fake_redis.items), 1)
        self.assertEqual(fake_redis.items[0][0], 'votes')
        self.assertIn('"vote": "a"', fake_redis.items[0][1])


if __name__ == '__main__':
    unittest.main()
