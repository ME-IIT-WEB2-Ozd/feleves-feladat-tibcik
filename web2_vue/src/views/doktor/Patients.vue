<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Betegek</h1>
            </div>

                <router-link :to="{name: 'AddPatient'}" class="button is-primary">Új beteg</router-link>
            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Név</th>
                            <th>Születési dátum</th>
                            <th>TAJ szám</th>
                            <th>Neme</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="patient in patients" v-bind:key="patient.id">
                            <td>{{ patient.name }}</td>
                            <td>{{ patient.szul_date }}</td>
                            <td>{{ patient.taj }}</td>
                            <td>{{ patient.nem }}</td>
                            <td>
                                <router-link :to="{name: 'Patient', params: {id: patient.id}}">Megtekint</router-link>
                            </td>
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
    name: 'Patients',
    data() {
        return {
            patients: []
        }
    },
    mounted() {
        this.getPatients()
    },
    methods: {
        async getPatients() {
            await axios
                .get('/api/v1/patients')
                .then(response => {
                    this.patients = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>