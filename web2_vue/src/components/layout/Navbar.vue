<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>Beteg nyílvántartó</strong>
            </router-link>
        </div>
        <div class="navbar-menu">
            <div class="navbar-end">
                <router-link :to="{name: 'Patients'}" class="navbar-item">Betegek</router-link>
                <router-link :to="{name: 'Tests'}" class="navbar-item">Szűrővizsgálatok</router-link>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        name: 'Navbar'
    }
</script>