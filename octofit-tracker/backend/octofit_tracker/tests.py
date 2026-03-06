from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        t = Team.objects.create(name='Test Team')
        u = User.objects.create(name='Test User', email='test@example.com', team=t)
        self.assertEqual(str(u), 'test@example.com')
    def test_activity_create(self):
        t = Team.objects.create(name='Test Team')
        u = User.objects.create(name='Test User', email='test@example.com', team=t)
        a = Activity.objects.create(user=u, type='Run', duration=10, date='2023-01-01')
        self.assertEqual(a.type, 'Run')
    def test_workout_create(self):
        w = Workout.objects.create(name='W1', description='desc', suggested_for='all')
        self.assertEqual(w.name, 'W1')
    def test_leaderboard_create(self):
        t = Team.objects.create(name='Test Team')
        l = Leaderboard.objects.create(team=t, points=42)
        self.assertEqual(l.points, 42)
