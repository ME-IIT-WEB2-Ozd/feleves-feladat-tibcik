<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ patient.name }}</h1>
            </div>

            <template v-if="!treat">
                <div class="column is-3">
                    <button class="button is-primary is-fullwidth" @click="treat = true">Új kezelés</button>
                </div>
                <div class="column is-3">
                    <router-link :to="{name: 'EditPatient', params: {id: patient.id}}" class="button is-info is-fullwidth">Beteg adatainak szerkesztése</router-link>
                </div>
                <div class="column is-3">
                </div>
                <div class="column is-3">
                    <button class="button is-danger is-fullwidth" @click="deletePatient">Beteg törlése</button>
                </div>
            </template>
            <template v-else>
                <div class="column is-3">
                    <button class="button is-primary is-fullwidth" @click="submitTreatment">Kezelés mentése</button>
                </div>
                <div class="column is-3">
                </div>
                <div class="column is-3">
                </div>
                <div class="column is-3">
                    <button class="button is-danger is-fullwidth" @click="treat = false">Vissza</button>
                </div>
            </template>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Adatok</h2>

                    <p><strong>Név: </strong>{{ patient.name }}</p>
                    <p><strong>Születési dátum: </strong>{{ patient.szul_date }}</p>
                    <p><strong>TAJ száma: </strong>{{ patient.taj }}</p>
                    <p><strong>Neme: </strong>{{ patient.name }}</p>
                </div>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Szükséges szűrővizsgálatok</h2>
                    <div v-for="test in tests" class="content">
                        {{ test.name }}
                        <button class="button is-small is-primary" @click="setTest(test.id)">Megjelent</button>
                    </div>
                </div>
            </div>
        </div>

        <template v-if="treat">
            <div class="column is-12">
                <form @submit.prevent="submitTreatment">
                    <div class="fields">
                        <label>Kezelés</label>
                        <textarea class="textarea is-primary" v-model="treatment.kezeles"></textarea>
                    </div>
                    <div class="fields">
                        <label>Gyógyszerek</label>
                        <p v-for="(medicine, index) in treatment.medicines"><input class="input" v-model="medicine.value" :key="index"></p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-success" @click="addMedicine">Új gyógyszer</button>
                        </div>
                    </div>
                </form>
            </div>
        </template>

        <article class="message is-dark">
            <div class="message-body">
                <div class="columns is-multiline" v-for="treatment in treatments">
                    <div class="column is-8">
                        <div class="box">
                            <h2 class="subtitle">{{ formatDate(treatment.ido) }}</h2>
                            <p>{{ treatment.kezeles }}</p>
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="box">
                            <h2 class="subtitle">Felírt gyógyszerek</h2>
                            <div class="content">
                                <ul v-for="medicine in treatment.medicines">
                                    <li>{{ medicine.gyogyszer }}</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="column is-12">
                        <div class="divider">.</div>
                    </div>
                </div>
            </div>
        </article>
    </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
    name: 'Patient',
    data() {
        return {
            patient: { id: -1 },
            treatments: [],
            treat: false,
            treatment: {
                kezeles: '',
                medicines: [{}]
            },
            tests: []
        }
    },
    mounted() {
        this.getPatient()
        this.getTreatments()
        this.getTests()
    },
    methods: {
        async getPatient() {
            const patientID = this.$route.params.id

            await axios
                .get(`/api/v1/patients/${patientID}/`)
                .then(response => {
                    this.patient = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async deletePatient() {
            const patientID = this.$route.params.id

            await axios
                .delete(`/api/v1/patients/${patientID}/`)
                .then(response => {
                    this.$router.push({name: 'Patients'})
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async getTreatments() {
            const patientID = this.$route.params.id

            await axios
                .get(`/api/v1/treatments/${patientID}/`)
                .then(response => {
                    this.treatments = response.data

                    this.treatments.forEach((treatment) => {
                        const treatmentID = treatment.id

                        axios
                            .get(`/api/v1/medicines/${treatmentID}/`)
                            .then(response => {
                                treatment.medicines = response.data
                            })
                            .catch(error => {
                                console.log(error)
                            })
                    })
                })
                .catch(error => {
                    console.log(error)
                })
        },
        formatDate(value){
         if (value) {
           return moment(String(value)).format('YYYY-MM-DD HH:MM')
          }
      },
      async submitTreatment() {
          const treatment = {
              patient: this.patient.id,
              kezeles: this.treatment.kezeles
          }

          await axios
                .post('/api/v1/treatments/', treatment)
                .then(response => {
                    this.treat = false

                    this.treatment.medicines.forEach((medicine) => {
                        const medicine_data = {
                            treatment: response.data.id,
                            gyogyszer: medicine['value']
                        }

                        axios
                            .post('/api/v1/medicines/', medicine_data)
                            .then(response => {

                            })
                            .catch(error => {
                                console.log(error)
                            })
                    })

                    this.getTreatments()
                })
                .catch(error => {
                    console.log(error)
                })
      },
      addMedicine(e) {
          this.treatment.medicines.push({})
          e.preventDefault();
      },
      async getTests() {
        const patientID = this.$route.params.id

        await axios
            .get(`/api/v1/tests/get_needed_tests/${patientID}/`)
            .then(response => {
                this.tests = response.data
            })
            .catch(error => {
                console.log(error)
            })
      },
      async setTest(testID) {
          const test = {
              patient: this.$route.params.id,
              test: testID
          }

          await axios
            .put('/api/v1/testeds/test/', test)
            .then(response => {
                this.getTests()
            })
            .catch(error => {
                console.log(error)
            })
      }
    }
}
</script>