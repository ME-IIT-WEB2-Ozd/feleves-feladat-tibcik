import { createRouter, createWebHistory } from 'vue-router'

import Patients from '../views/doktor/Patients.vue'
import Patient from '../views/doktor/Patient.vue'
import AddPatient from '../views/doktor/AddPatient.vue'
import EditPatient from '../views/doktor/EditPatient.vue'
import Tests from '../views/doktor/Tests.vue'
import AddTest from '../views/doktor/AddTest.vue'

const routes = [
  {
    path: '/',
    name: 'Betegek',
    component: Patients
  },
  {
    path: '/doctor/patients',
    name: 'Patients',
    component: Patients,
  },
  {
    path: '/doctor/patient/:id',
    name: 'Patient',
    component: Patient,
  },
  {
    path: '/doctor/add_patient',
    name: 'AddPatient',
    component: AddPatient,
  },
  {
    path: '/doctor/edit_patient/:id',
    name: 'EditPatient',
    component: EditPatient,
  },
  {
    path: '/doctor/tests/',
    name: 'Tests',
    component: Tests,
  },
  {
    path: '/doctor/add_test/',
    name: 'AddTest',
    component: AddTest,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
