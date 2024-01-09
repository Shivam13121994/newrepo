from rest_framework.throttling import UserRateThrottle

class ShivamRateThrottle(UserRateThrottle):
    scope = 'Shivam'
    