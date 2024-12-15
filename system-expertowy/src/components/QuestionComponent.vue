<template>
    <div class="card p-3">
  <h5 class="card-title">{{ question }}</h5>
  <div class="row justify-content-between">
    <div class="col-6 col-md-6">
      <button 
        class="btn btn-success"
        @click="sendAnswer(1)"
      >
        {{ positiveAnswerText }}
      </button>
    </div>
    <div class="col-6 col-md-6">
      <button 
        class="btn btn-danger"
        @click="sendAnswer(0)"
      >
        {{ negativeAnswerText }}
      </button>
    </div>
  </div>
</div>

  </template>
  
  <script>
  export default {
    name: 'QuestionComponent',
    props: {
      question: {
        type: String,
        required: true
      },
      positiveAnswerText: {
        type: String,
        required: true
      },
      negativeAnswerText: {
        type: String,
        required: true
      }
    },
    methods: {
      sendAnswer(answer) {
        this.$emit('answer-selected', answer);
      }
    }
  };
  </script>
  
  <style scoped>
  .card {
    max-width: 400px;
    margin: auto;
  }
  </style>
  