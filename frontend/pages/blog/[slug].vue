<template>
  <NavBarDark/>
  <div v-if="blogStore.isLoading" class="loading">
    Loading...
  </div>
  <div v-else-if="blogStore.error" class="error">
    {{ blogStore.error }}
  </div>
  <div v-else-if="blog" class="blog-detail">
    <!-- ... (previous content remains the same) ... -->

    <div class="comments-section">
      <h2>Comments ({{ blog.comments_count }})</h2>
      <div class="comment-form">
        <textarea v-model="newComment" placeholder="Write your comment here..."></textarea>
        <input v-model="authorName" placeholder="Your Name"/>
        <button @click="submitComment" :disabled="isCommentButtonDisabled" class="post-comment-btn">
          {{ isCommentButtonDisabled ? `Wait ${cooldownTime}s` : 'Post Comment' }}
        </button>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      </div>
      <div class="comments-list">
        <Comment v-for="comment in blog.comments" :key="comment.id" :comment="comment" :blogSlug="blog.slug" @reply="handleReply"/>
      </div>
    </div>
  </div>
  <div v-else class="no-blog">
    <p>Blog post not found.</p>
  </div>
  <BottomBar/>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useBlogStore } from '@/stores/blogStore';
import { useRouter, useRoute } from 'vue-router';
import NavBarDark from '@/components/NavBarDark.vue';
import BottomBar from '@/components/BottomBar.vue';
import Comment from '@/components/Comment.vue';

const blogStore = useBlogStore();
const route = useRoute();
const slug = route.params.slug;
const blog = computed(() => blogStore.currentBlog);

const newComment = ref('');
const authorName = ref('');
const errorMessage = ref('');
const isCommentButtonDisabled = ref(false);
const cooldownTime = ref(15);

const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};

const submitComment = async () => {
  if (newComment.value && authorName.value && blog.value) {
    try {
      await blogStore.postComment(blog.value.slug, {
        body: newComment.value,
        author: authorName.value
      });
      newComment.value = '';
      authorName.value = '';
      errorMessage.value = '';
      startCooldown();
    } catch (error) {
      errorMessage.value = error.response?.data?.detail || 'Failed to submit comment';
    }
  }
};

const startCooldown = () => {
  isCommentButtonDisabled.value = true;
  let remainingTime = 15;
  const timer = setInterval(() => {
    cooldownTime.value = remainingTime;
    remainingTime--;
    if (remainingTime < 0) {
      clearInterval(timer);
      isCommentButtonDisabled.value = false;
      cooldownTime.value = 15;
    }
  }, 1000);
};

const fetchBlog = async () => {
  await blogStore.fetchBlogBySlug(slug);
};

const handleReply = async (replyData) => {
  try {
    await blogStore.postComment(blog.value.slug, replyData);
  } catch (error) {
    console.error('Failed to post reply', error);
  }
};

onMounted(fetchBlog);
</script>

<style scoped>
.blog-detail {
  max-width: 80%;
  margin: 0 auto;
  padding: 20px;
}

.tags {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 20px;
}

.tag {
  background-color: #f0f0f0;
  padding: 5px 10px;
  border-radius: 15px;
  font-size: 0.9em;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.blog-detail img {
  display: block;
  width: 100%;
  max-width: 600px;
  height: 400px;
  object-fit: cover;
  margin: 0 auto;
}

.meta {
  margin-top: 20px;
  text-align: center;
}

.comments-section {
  margin-top: 40px;
}

.comment-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
}

.comment-form textarea, .comment-form input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.post-comment-btn {
  align-self: flex-end;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.comments-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.loading, .error, .no-blog {
  text-align: center;
  margin: 20px 0;
  font-size: 1.2rem;
}

.error {
  color: red;
}

:deep(p) {
  margin-bottom: 1em;
}

:deep(h2) {
  margin-top: 1.5em;
}

:deep(ul, ol) {
  margin-left: 2em;
  margin-bottom: 1em;
}
</style>
