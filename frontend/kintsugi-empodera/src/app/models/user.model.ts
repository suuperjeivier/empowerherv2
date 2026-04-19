export interface User {
  id: number;
  email: string;
  username: string;
  full_name?: string;
  role: 'student' | 'admin';
  is_active: boolean;
  profile_image?: string;
  created_at: string;
}

export interface UserCreate {
  email: string;
  username: string;
  password: string;
  full_name?: string;
}

export interface UserLogin {
  username: string;
  password: string;
}

export interface AuthToken {
  access_token: string;
  token_type: string;
}

// Made with Bob
