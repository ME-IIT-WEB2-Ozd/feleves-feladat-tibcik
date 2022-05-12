<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Új teszt</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="fields">
                        <label>Leírás</label>
                        <div class="control">
                            <input type="text" class="input" v-model="name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Neme</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="nem">
                                    <option value="f">Férfi</option>
                                    <option value="n">Nő</option>
                                    <option value="m">Mindekttő</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="fields">
                        <label>Kezdő kor</label>
                        <div class="control">
                            <input type="number" class="input" v-model="kor">
                        </div>
                    </div>

                    <div class="fields">
                        <label>Időköz(év)</label>
                        <div class="control">
                            <input type="number" class="input" v-model="interval">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Mentés</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { toast } from 'bulma-toast'

export default {
    name: 'AddTest',
    data() {
        return {
            name: '',
            nem: 'm',
            kor: 0,
            interval: 1,
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if(this.name === '')
                this.errors.push("A teszt leírássát meg kell adni!") 
            
            if(this.kor < 0)
                this.errors.push('A kezdő kor nem lehen 0-nál kissebb!')

            if(this.interval <= 0)
                this.errors.push('Az időküz nem lehet 1 évnél kisebb!')

            if(this.errors.length)
                return

            const test = {
                name: this.name,
                nem: this.nem,
                kor: this.kor,
                interval: this.interval,
            }

            await axios
                .post('/api/v1/tests/', test)
                .then(response => {
                    toast({
                        message: 'Teszt hozzáadva',
                        type: 'is-succes',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })

                    this.$router.push({name: 'Tests'})
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else if (error.message) {
                        this.errors.push('Hiba történt! Kérem próbálja meg később.')
                    }
                })
        }
    }
}
</script>