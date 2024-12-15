import HomePageComponent from "./components/HomePageComponent.vue"
import QuestionCollectorComponent from "./components/QuestionCollectorComponent.vue";
import ResultPageCpompnent from "./components/ResultPageCpompnent.vue";

import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomePageComponent
    },
    {
        path: '/questions',
        name: 'Questions',
        component: QuestionCollectorComponent
    },
    {
        path: '/resume/:lang',
        name: 'Result',
        component: ResultPageCpompnent
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;