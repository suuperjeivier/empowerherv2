import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CommunityService } from '../../services/community.service';
import { CommunityPost } from '../../models/community.model';

@Component({
  selector: 'app-community',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: '<div class="community-container"><h1>Comunidad</h1><p>Conecta con otras mujeres empoderadas</p></div>',
  styles: ['.community-container { padding: 2rem; }']
})
export class CommunityComponent implements OnInit {
  posts: CommunityPost[] = [];
  newPostContent = '';

  constructor(private communityService: CommunityService) {}

  ngOnInit(): void {
    this.loadPosts();
  }

  loadPosts(): void {
    this.communityService.getCommunityPosts().subscribe({
      next: (posts) => this.posts = posts,
      error: (error) => console.error('Error loading posts:', error)
    });
  }

  createPost(): void {
    if (this.newPostContent.trim()) {
      this.communityService.createPost({ content: this.newPostContent }).subscribe({
        next: () => {
          this.newPostContent = '';
          this.loadPosts();
        },
        error: (error) => console.error('Error creating post:', error)
      });
    }
  }
}

// Made with Bob
