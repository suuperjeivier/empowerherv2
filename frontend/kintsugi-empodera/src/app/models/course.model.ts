export interface Course {
  id: number;
  title: string;
  description?: string;
  icon?: string;
  color?: string;
  duration_hours?: number;
  difficulty_level?: string;
  is_active: boolean;
  created_at: string;
}

export interface Module {
  id: number;
  course_id: number;
  title: string;
  description?: string;
  order: number;
  is_locked: boolean;
  created_at: string;
}

export interface Lesson {
  id: number;
  module_id: number;
  title: string;
  content?: string;
  video_url?: string;
  order: number;
  duration_minutes?: number;
  created_at: string;
}

export interface Enrollment {
  id: number;
  user_id: number;
  course_id: number;
  enrolled_at: string;
  completed_at?: string;
  progress_percentage: number;
}

export interface Progress {
  id: number;
  user_id: number;
  module_id: number;
  is_completed: boolean;
  completed_at?: string;
  created_at: string;
}

export interface CourseProgress {
  course: Course;
  progress_percentage: number;
  completed_modules: number;
  total_modules: number;
}

export interface DashboardStats {
  total_courses: number;
  completed_courses: number;
  in_progress_courses: number;
  total_achievements: number;
  overall_progress: number;
}

// Made with Bob
