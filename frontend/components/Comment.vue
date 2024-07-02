<script setup>
import { ref, computed } from 'vue';
import { useBlogStore } from '@/stores/blogStore';

const props = defineProps({
  comment: Object,
  blogSlug: String,
  nestedLevel: {
    type: Number,
    default: 0
  }
});

const emit = defineEmits(['reply']);

const blogStore = useBlogStore();

const replyBody = ref('');
const replyAuthor = ref('');
const errorMessage = ref('');
const showReplyForm = ref(false);

const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};

const toggleReplyForm = () => {
  showReplyForm.value = !showReplyForm.value;
};

const submitReply = async () => {
  if (replyBody.value && replyAuthor.value) {
    try {
      await emit('reply', {
        parent_id: props.comment.id,
        body: replyBody.value,
        author: replyAuthor.value
      });
      replyBody.value = '';
      replyAuthor.value = '';
      errorMessage.value = '';
      showReplyForm.value = false;
    } catch (error) {
      errorMessage.value = 'Error posting reply: ' + error.message;
    }
  } else {
    errorMessage.value = 'Please fill out all fields';
  }
};

const nestedComments = computed(() => props.comment.replies || []);
</script>

<template>
  <div class="comment" :style="{ marginLeft: `${props.nestedLevel * 20}px` }">
    <p class="comment-body">{{ comment.body }}</p>
    <p class="comment-meta">
      By {{ comment.author }} on {{ formatDate(comment.created_at) }}
    </p>
    <button @click="toggleReplyForm" class="reply-btn">Reply</button>
    <div v-if="showReplyForm" class="reply-form">
      <textarea v-model="replyBody" placeholder="Write your reply here..."></textarea>
      <input v-model="replyAuthor" placeholder="Your Name"/>
      <button @click="submitReply" class="post-reply-btn">Post Reply</button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
    <div v-if="nestedComments.length > 0" class="nested-comments">
      <Comment
          v-for="nestedComment in nestedComments"
          :key="nestedComment.id"
          :comment="nestedComment"
          :blogSlug="blogSlug"
          :nestedLevel="props.nestedLevel + 1"
          @reply="$emit('reply', $event)"
      />
    </div>
  </div>
</template>

<style scoped>
.comment {
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.comment-body {
  margin-bottom: 10px;
}

.comment-meta {
  font-size: 0.8em;
  color: #666;
}

.reply-btn {
  background: none;
  border: none;
  color: #007bff;
  cursor: pointer;
  margin-top: 10px;
}

.reply-form {
  margin-top: 10px;
}

.reply-form textarea, .reply-form input {
  width: 100%;
  padding: 5px;
  margin-bottom: 5px;
}

.post-reply-btn {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}

.error {
  color: red;
}

.nested-comments {
  margin-left: 20px;
}
</style>