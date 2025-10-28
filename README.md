# Barangay Tindahan Compliance Tracker

A FastAPI MVC application for barangay officials to monitor and enforce compliance of local tindahan, street hawkers, and peddlers. Built with modern web technologies and following the Vibecamp design system.

**A Vibecamp Creation**

## 🚀 Features

- **Tindahan Registration**: Register and track all local businesses (tindahan, street hawkers, peddlers)
- **Compliance Inspections**: Schedule and conduct regular compliance inspections
- **Violation Tracking**: Track violations and monitor resolution progress
- **Permit Management**: Monitor business permits and expiry dates
- **Compliance Reports**: Generate comprehensive compliance reports and analytics
- **Mobile-First Design**: Responsive interface optimized for mobile devices
- **Real-time Monitoring**: Live compliance status updates and alerts

## 🏗️ Architecture

This project follows the FastAPI MVC pattern with clear separation of concerns:

```
app/
├── models/          # Database models (Tindahan, Inspections, Violations, Reports)
├── controllers/     # Business logic layer
├── routes/          # API route definitions
├── templates/       # Jinja2 templates with TailwindCSS
├── utils/           # Utility functions
└── database.py      # Database configuration
```

## 🛠️ Tech Stack

- **Backend**: FastAPI 0.104.1
- **Database**: SQLite with SQLModel/SQLAlchemy
- **Frontend**: Jinja2 templates with TailwindCSS
- **Styling**: Vibecamp Design System (black & white theme)
- **Deployment**: Docker + Fly.io
- **Python**: 3.11+

## 📋 Prerequisites

- Python 3.11 or higher
- pip or Poetry for dependency management
- Git for version control

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd brgy-tindahan-tracker
```

### 2. Install Dependencies

Using pip:
```bash
pip install -r requirements.txt
```

Using Poetry:
```bash
poetry install
```

### 3. Run the Application

```bash
# Using uvicorn directly
uvicorn main:app --reload

# Or using Python
python main.py
```

### 4. Access the Application

- **Web Interface**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📱 Usage

### Tindahan Registration
1. Navigate to the "Tindahan" page
2. Click "Register Tindahan" to register a new business
3. Fill in business details (name, owner, type, address, permit info)
4. Manage existing registrations with edit/update options

### Compliance Inspections
1. Go to the "Inspections" page
2. Schedule new inspections for registered businesses
3. Conduct inspections and record findings
4. Track inspection history and follow-ups

### Violation Tracking
1. Visit the "Violations" page
2. View all active violations and their status
3. Update violation resolution progress
4. Monitor compliance improvement

### Compliance Reports
1. Navigate to the "Reports" page
2. Generate compliance reports by period or zone
3. View compliance metrics and analytics
4. Export reports for official use

## 🎨 Design System

This application follows the **Vibecamp Design System**:

- **Colors**: Pure black and white aesthetic
- **Typography**: Kalam (handwritten) for headings, Inter for body text
- **Components**: Consistent card layouts, forms, and navigation
- **Mobile-First**: Responsive design optimized for mobile devices
- **Branding**: Vibecamp logo and "A Vibecamp Creation" attribution

## 🗄️ Database Schema

### Tindahan
- Business information (name, owner, type, address, contact)
- Permit details (number, issue date, expiry date)
- Compliance status and inspection tracking
- Barangay zone assignment

### Inspections
- Inspection records (type, date, inspector, status)
- Inspection notes and findings
- Follow-up scheduling

### Violations
- Violation details (type, description, severity)
- Resolution tracking and status
- Associated inspection records

### Compliance Reports
- Generated compliance reports
- Metrics and analytics data
- Report period and scope

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=sqlite+aiosqlite:///./brgy_tindahan.db
DEBUG=True
```

### Database Migration

The application automatically creates database tables on startup. For production, consider using Alembic for migrations:

```bash
# Initialize Alembic (if not already done)
alembic init migrations

# Create a migration
alembic revision --autogenerate -m "Initial migration"

# Apply migrations
alembic upgrade head
```

## 🚀 Deployment

### Using Docker

1. Build the Docker image:
```bash
docker build -t brgy-tindahan-tracker .
```

2. Run the container:
```bash
docker run -p 8000:8000 brgy-tindahan-tracker
```

### Using Fly.io

1. Install Fly CLI: https://fly.io/docs/hands-on/install-flyctl/

2. Login to Fly.io:
```bash
fly auth login
```

3. Deploy the application:
```bash
fly deploy
```

4. Open the deployed app:
```bash
fly open
```

## 🧪 Testing

Run the test suite:

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

## 📊 API Endpoints

### Tindahan
- `GET /api/v1/tindahan` - List all registered businesses
- `POST /api/v1/tindahan` - Register a new business
- `GET /api/v1/tindahan/{id}` - Get business by ID
- `PUT /api/v1/tindahan/{id}` - Update business information
- `DELETE /api/v1/tindahan/{id}` - Deactivate business registration

### Inspections
- `GET /api/v1/inspections` - List all inspections
- `POST /api/v1/inspections` - Schedule new inspection
- `GET /api/v1/inspections/{id}` - Get inspection details
- `PUT /api/v1/inspections/{id}` - Update inspection status

### Violations
- `GET /api/v1/violations` - List all violations
- `POST /api/v1/violations` - Record new violation
- `PUT /api/v1/violations/{id}` - Update violation status

### Compliance Reports
- `GET /api/v1/reports` - List generated reports
- `POST /api/v1/reports` - Generate new report
- `GET /api/v1/compliance/metrics` - Get compliance metrics

### Health Check
- `GET /health` - Application health status

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Vibecamp** for the design system and inspiration
- **FastAPI** for the excellent web framework
- **TailwindCSS** for the utility-first CSS framework
- **SQLModel** for the modern ORM

## 📞 Support

For support and questions:
- Create an issue in the GitHub repository
- Contact the development team

---

**A Vibecamp Creation** - Building tools for the community, by the community.