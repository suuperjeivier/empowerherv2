# Kintsugi Empodera - Frontend

Angular application for the Kintsugi Empodera learning platform.

## Features

Based on the design, this application includes 12 main screens:

1. **Onboarding/Welcome** - Introduction to the platform
2. **Home (Inicio)** - Dashboard with daily phrase, progress overview, and quick actions
3. **Courses (Cursos)** - Browse and enroll in available courses
4. **Course Detail** - View course modules and lessons
5. **Progress & Achievements** - Track learning progress and earned achievements
6. **Calendar & Planner** - Schedule and manage learning activities
7. **Community** - Connect and share with other learners
8. **Profile** - User profile and settings
9. **Emotional State** - Track and log emotional well-being
10. **Daily Phrases** - Inspirational quotes and affirmations
11. **Notifications** - Stay updated with platform activities
12. **Settings** - Customize app preferences

## Prerequisites

- Node.js 18+ and npm
- Angular CLI 17+

## Installation

1. Navigate to the frontend directory:
```bash
cd frontend/kintsugi-empodera
```

2. Install dependencies:
```bash
npm install
```

3. Update the API URL in `src/environments/environment.ts` if needed:
```typescript
export const environment = {
  production: false,
  apiUrl: 'http://localhost:8000'
};
```

## Development

Run the development server:
```bash
ng serve
```

Navigate to `http://localhost:4200/`. The application will automatically reload if you change any source files.

## Build

Build the project for production:
```bash
ng build --configuration production
```

The build artifacts will be stored in the `dist/` directory.

## Project Structure

```
src/
├── app/
│   ├── components/          # UI components for all 12 screens
│   │   ├── onboarding/
│   │   ├── login/
│   │   ├── register/
│   │   ├── home/
│   │   ├── courses/
│   │   ├── course-detail/
│   │   ├── progress/
│   │   ├── calendar/
│   │   ├── community/
│   │   ├── profile/
│   │   ├── emotional/
│   │   ├── daily-phrases/
│   │   ├── notifications/
│   │   └── settings/
│   ├── models/              # TypeScript interfaces
│   │   ├── user.model.ts
│   │   ├── course.model.ts
│   │   └── community.model.ts
│   ├── services/            # API services
│   │   ├── auth.service.ts
│   │   ├── course.service.ts
│   │   ├── progress.service.ts
│   │   └── community.service.ts
│   ├── guards/              # Route guards
│   │   └── auth.guard.ts
│   ├── interceptors/        # HTTP interceptors
│   │   └── auth.interceptor.ts
│   ├── app.config.ts        # App configuration
│   └── app.routes.ts        # Route definitions
├── environments/            # Environment configurations
├── styles.scss              # Global styles
└── index.html
```

## Key Technologies

- **Angular 17+** - Standalone components with signals
- **RxJS** - Reactive programming
- **SCSS** - Styling
- **TypeScript** - Type safety

## API Integration

The frontend communicates with the FastAPI backend through HTTP services:

- **AuthService** - User authentication and registration
- **CourseService** - Course management and enrollment
- **ProgressService** - Track learning progress
- **CommunityService** - Community posts, emotional logs, notifications, and daily phrases

All API requests are automatically authenticated using the JWT token stored in localStorage via the `authInterceptor`.

## Routing

The application uses lazy-loaded routes for optimal performance:

- Public routes: `/onboarding`, `/login`, `/register`
- Protected routes (require authentication): All other routes
- Default redirect: `/onboarding` → `/home` (when authenticated)

## Styling

The application uses a custom design system with:

- Color palette inspired by the Kintsugi philosophy
- Responsive design for mobile and desktop
- Smooth animations and transitions
- Accessible UI components

### Color Scheme

- Primary: Purple (#8B5CF6) - Represents growth and transformation
- Secondary: Pink (#EC4899) - Represents empowerment
- Accent: Amber (#F59E0B) - Represents achievement
- Success: Green (#10B981)
- Error: Red (#EF4444)

## Development Guidelines

1. **Components**: Use standalone components with the `standalone: true` flag
2. **Services**: Inject services using constructor injection
3. **State Management**: Use RxJS BehaviorSubjects for shared state
4. **Styling**: Use SCSS with component-scoped styles
5. **Type Safety**: Always define TypeScript interfaces for data models

## Testing

Run unit tests:
```bash
ng test
```

Run end-to-end tests:
```bash
ng e2e
```

## Deployment

1. Build for production:
```bash
ng build --configuration production
```

2. Deploy the `dist/kintsugi-empodera` folder to your hosting service

3. Update `src/environments/environment.prod.ts` with your production API URL

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

Private - All rights reserved
