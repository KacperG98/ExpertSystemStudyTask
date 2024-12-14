<template>
  <div class="container">
    <div v-for="(question, index) in questions" :key="index" class="row m-5">
      <QuestionAnswerComponent 
          :question="question.txt"
          :positiveAnswerText="question.positiveTxt"
          :negativeAnswerText="question.negativeTxt"
          @answer-selected="a => setAnswer(a, index)"
      />
    </div>
    
    <div v-if="result.length > 0" class="card m-4">
      <div class="card-body">
        {{ result }}
      </div>
    </div>

    <button class="btn btn-primary btn-lg m-4" @click="submitAnswers">Wyślij odpowiedzi</button>
  </div>
</template>


<script>
import QuestionAnswerComponent from './components/QuestionAnswerComponent.vue';

export default {
  name: 'App',
  components: {
    QuestionAnswerComponent
  },
  data() {
    return {
      questions: [
        {txt: "Jaki język być wolał?", positiveTxt: "Interpretowany", negativeTxt: "Kompilowany"},
        {txt: "czy chcesz tworzyć strony i aplikacje www?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy chcesz robić elementy wizuane na stronach?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy zależy ci naprostym wejściu na rynek?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy zależy ci na większej popularności języka?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy chcesz przetwarzać dane", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Chciałbyś pracować w środowisku akademickim?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy chcesz zarządzać systemem?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy lubisz deykowane środowiska?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy lubisz firme Oracle?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy chcesz tworzyć aplikacje na telefon?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy chcesz robić telko dla IOS?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Wsparcie któ©ej firmy byś wolał?", positiveTxt: "Google", negativeTxt: "Microsoft"},
        {txt: "Czy chcesz robić aplikacje pod desktop?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy aplikacje z UI?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy chcesz tworzyć gry?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy to mają być duże produkcje?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Jak bardzo zależy ci na wydajności?", positiveTxt: "Bardzo", negativeTxt: "Bez różnicy"},
        {txt: "Czy chcesz robić aplikacje na mikrokontrolery?", positiveTxt: "Tak", negativeTxt: "Nie"},
        {txt: "Czy chcesz uczyć się nowych technologii?", positiveTxt: "Tak", negativeTxt: "Nie"}
      ],
      answerlist: Array(20).fill(0),
      result: ""
    };
  },
  methods: {
    setAnswer(answer, index) {
      this.answerlist[index] = answer;
      console.log(this.answerlist)
    },
    async submitAnswers() {
      const url = 'http://localhost:5000/lang'; // Adres endpointa
      const data = this.answerlist;

      try {
        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        });

        if (!response.ok) {
          throw new Error(`Error: ${response.status}`);
        }

        const result = await response.json();
        console.log('Response:', result);
        this.result = result[0];
      } catch (error) {
        console.error('Request failed:', error);
      }
    }
  }
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
