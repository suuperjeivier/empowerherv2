export interface CommunityPost {
  id: number;
  user_id: number;
  content: string;
  likes_count: number;
  comments_count: number;
  created_at: string;
  updated_at?: string;
}

export interface CommunityPostCreate {
  content: string;
}

export type EmotionalState = 'happy' | 'calm' | 'anxious' | 'content' | 'tired' | 'frustrated';

export interface EmotionalLog {
  id: number;
  user_id: number;
  emotional_state: EmotionalState;
  note?: string;
  created_at: string;
}

export interface EmotionalLogCreate {
  emotional_state: EmotionalState;
  note?: string;
}

export interface Notification {
  id: number;
  user_id: number;
  title: string;
  message: string;
  is_read: boolean;
  notification_type?: string;
  created_at: string;
}

export interface DailyPhrase {
  id: number;
  phrase: string;
  author?: string;
  category?: string;
  created_at: string;
}

export interface CalendarEvent {
  id: number;
  user_id: number;
  title: string;
  description?: string;
  event_date: string;
  event_type?: string;
  created_at: string;
}

// Made with Bob
