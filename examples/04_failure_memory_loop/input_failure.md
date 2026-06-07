# Failed Agent Session Summary

The task was: "Add a simple in-memory cache around the user profile fetch so we stop hitting the auth service on every page view."

The agent:
- Wrapped the profile call with a 60-second TTL cache.
- Made the cache key only the user id.
- Cleared the cache on any "profile updated" event it could find.
- All unit tests for the profile module passed.
- The change was merged.

Two days later:
- Users started seeing stale profile data (avatar, display name, role) after they updated their profile via the mobile app.
- The mobile app uses a different update path that did not emit the event the web cache was listening for.
- Several support tickets and one angry enterprise customer.

The root cause was that the cache invalidation was incomplete for the full set of update surfaces. The agent only considered the web client surfaces it was shown.