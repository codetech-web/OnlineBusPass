# Online Bus Pass Management System

Academic project built with React JS + Python Django REST. **No MySQL/database is required.** Demo data is stored in Python memory and resets when Django restarts.

## Features
- Creative responsive student dashboard
- Online bus pass application wizard
- Pass type and route selection
- Document checklist
- Application tracking with search/filter
- Digital bus pass + QR-style verification card
- Pass renewal/expiry-ready workflow
- Officer/Admin application queue
- Approve/reject workflow
- Priority and document verification status
- Analytics dashboard and monthly charts
- Notifications and expiry alerts
- Feedback and star rating
- Profile/settings
- FAQ/help centre
- REST API architecture
- Demo data for presentation/viva

## Demo login
Student: `student@demo.com` / `student123`
Officer: `officer@demo.com` / `officer123`

## Run in VS Code
### Backend
```bash
cd backend
python -m venv venv
# Windows
venv\\Scripts\\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
Backend: http://127.0.0.1:8000/

### Frontend (new terminal)
```bash
cd frontend
npm install
npm run dev
```
Frontend: http://localhost:5173/

**No `migrate` and no MySQL setup are needed.** Django uses a dummy DB engine only so the framework can run without a real database.

## API
`GET /api/health/`, `/api/routes/`, `/api/pass-types/`, `/api/applications/`, `/api/applications/<id>/`, `/api/dashboard/`, `/api/notifications/`
`POST /api/applications/create/`, `POST /api/applications/<id>/feedback/`, `PATCH /api/applications/<id>/update/`

See `docs/PROJECT_MODULES.md` for viva points and future scope.
