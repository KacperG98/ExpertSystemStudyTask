<template>
    <div class="container">
      <div class="row">
  
        <div class="col">
          <QuestionComponent 
          :question="question"
          :positiveAnswerText="positiveAnswerText"
          :negativeAnswerText="negativeAnswerText"
          @answer-selected="handleAnswer"/>
        </div>
        
        <div class="col alert alert-success">
          <h5 class="p-3">Odpowiedź użytkownika: {{ convertAnswer(userAnswer) }}</h5>
        </div>
        
      </div>
    </div>
  </template>
  
  <script>
  
  </script>
  
  <script>
  import QuestionComponent from './QuestionComponent.vue'
  
  export default {
    name: 'QuestionAnswerComponent',
    components: {
      QuestionComponent
    },
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
    data() {
      return {
        userAnswer: 2
      };
    },
    computed: {
      answersList() {
        return [this.negativeAnswerText, this.positiveAnswerText, 'Brak'];
      }
    },
    methods: {
      handleAnswer(answer) {
        this.userAnswer = answer;
        this.$emit('answer-selected', (answer == 2)? 0 : answer);
      },
      convertAnswer(answer){
        //let answersList = [this.negativeAnswerText, this.positiveAnswerText, 'Brak']
        return this.answersList[answer]
      }
    }
  }
  </script>
  