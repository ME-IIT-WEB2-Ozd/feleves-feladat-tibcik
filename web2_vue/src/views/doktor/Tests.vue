<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Szűrőviszgálatok</h1>
            </div>

                <router-link :to="{name: 'AddTest'}" class="button is-primary">Új szűrővizsgálat</router-link>
            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Leírás</th>
                            <th>Nem</th>
                            <th>Kortól</th>
                            <th>Időköz</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="test in tests" v-bind:key="test.id">
                            <td>{{ test.name }}</td>
                            <td>{{ test.nem }}</td>
                            <td>{{ test.kor }}</td>
                            <td>{{ test.interval }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Tests',
    data() {
        return {
            tests: []
        }
    },
    mounted() {
        this.getTests()
    },
    methods: {
        async getTests() {
            await axios
                .get('/api/v1/tests/')
                .then(response => {
                    this.tests = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>