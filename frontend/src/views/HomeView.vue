<template>
  <main>
    <v-data-table :items="items"></v-data-table>
  </main>
</template>

<script setup>

import {ref} from 'vue';

const items = ref[
    {
      name: 'African Elephant',
      species: 'Loxodonta africana',
      diet: 'Herbivore',
      habitat: 'Savanna, Forests',
    }
  ]

</script>