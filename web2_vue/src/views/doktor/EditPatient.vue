<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ patient.name }} Szerkesztése</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="fields">
                        <label>Név</label>
                        <div class="control">
                            <input type="text" class="input" v-model="patient.name">
                        </div>
                    </div>

                    <div class="fields">
                        <label>Születési idő</label>
                        <div class="control">
                            <input type="date" class="input" v-model="patient.szul_date">
                        </div>
                    </div>

                    <div class="fields">
                        <label>TAJ száma</label>
                        <div class="control">
                            <input type="text" class="input" v-model="patient.taj">
                        </div>
                    </div>

                    <div class="field">
                        <label>Neme</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="patient.nem">
                                    <option value="f" selected>Férfi</option>
                                    <option value="n">Nő</option>
                                </select>
                            </div>
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
    name: 'AddPatient',
    data() {
        return {
            patient: {
                nem: 'f'
            },
            errors: []
        }
    },
    mounted() {
        this.getPatient()
    },
    methods: {
        async getPatient() {
            const patientID = this.$route.params.id

            axios
                .get(`/api/v1/patients/${patientID}/`)
                .then(response => {
                    this.patient = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async submitForm() {
            this.errors = []

            if(this.patient.name === '')
                this.errors.push("A név mező kitöltése kötelező!") 
            
            if(this.patient.szul_date === '')
                this.errors.push('A születési dátum megadása kötelező!')

            if(this.patient.taj == '')
                this.errors.push('A TAJ szám megadása kötelező!')

            if(this.errors.length)
                return

            const patientID = this.$route.params.id

            await axios
                .put(`/api/v1/patients/${patientID}/`, this.patient)
                .then(response => {
                    toast({
                        message: 'Beteg adatai módosítva',
                        type: 'is-succes',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })

                    this.$router.push({name: 'Patient', params: {id: patientID}})
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