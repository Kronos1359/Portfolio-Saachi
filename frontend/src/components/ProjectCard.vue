<script setup>
    defineProps(['title', 'description', 'repoUrl', 'liveUrl'])
</script>
<template>
    <div class="project-card">
        <h2>{{ title }}</h2>
        <p>{{ description }}</p>

        <a 
            :href="repoUrl"
            class="repo-link"
            target="_blank" 
            rel="noopener noreferrer"
        >
            Source Code 
        </a>

        <a 
            v-if="liveUrl" 
            :href="liveUrl"
            class="live-link"
            target="_blank"
            rel="noopener noreferrer"
        >
            Live Demo
        </a>
    </div>
</template>