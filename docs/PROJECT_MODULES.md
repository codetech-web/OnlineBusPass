# Project Modules & Viva Notes

## Core modules
1. Student registration/profile
2. Online pass application
3. Pass type selection
4. Route selection
5. Document checklist
6. Application tracking and search
7. Status timeline
8. Officer verification
9. Approval/rejection
10. Digital pass and QR-style verification
11. Expiry/renewal workflow
12. Notifications
13. Feedback and rating
14. Analytics/reports
15. FAQ/help centre
16. Responsive UI

## Suggested final-year style extensions
- JWT/OTP login
- Real MySQL models for Student, Route, Pass, Application, Payment, Document and Feedback
- Payment gateway
- PDF pass generation
- Real QR scanner
- SMS/email notifications
- College verification portal
- GPS/live bus tracking
- Role-based access control
- Audit logs

## Why no database?
This version intentionally stores demo records in `backend/buspass_api/store.py`. Django is configured with a dummy database engine, so MySQL/SQLite and migrations are not required. Restarting Django resets demo data.
