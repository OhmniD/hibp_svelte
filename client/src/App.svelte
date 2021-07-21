<script>
import { onMount } from 'svelte';
import Modal from 'svelte-simple-modal';
import { emailsStore, totalBreachesStore } from './stores/stores.js'

	import Emails from './components/Email.svelte'
	import Form from './components/Form.svelte'

	let total_breaches = 0

	let emails

	async function getEmails() {
		let response = await fetch('http://localhost:8000/emails');

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}
		emails = await response.json()

		emails.map(email => total_breaches += email.num_of_breaches)
		totalBreachesStore.set(total_breaches)
		emailsStore.set(emails)
	}


	emailsStore.subscribe(value => {
		emails = value;
	});

	totalBreachesStore.subscribe(value => {
		total_breaches = value;
	});

	onMount(() => {
		getEmails()
	})
	
</script>

<main>
	<header>
		<h1>H I B P </h1>
		<Form />
	</header>
	<div id="total-breaches">
		
		<h2>Total Breaches: <strong>{total_breaches}</strong></h2>
	</div>
	<Modal>
		<Emails bind:emails={emails}/>
	</Modal>
	

</main>

<style>
	@import url('https://fonts.googleapis.com/css2?family=PT+Sans&family=Roboto&family=Anton&family=Signika:wght@300&display=swap');

	* {
		margin: 0;
		padding: 0;
	}

	header {
	background-color: #3e4451;
	background-image: linear-gradient(#3e4451, #282c34);
	display: flex;
	align-items: center;
	justify-content: space-between;
	padding-left: 4rem;
	height: 4rem;
	font-family: "PT Sans"
	}

	h2 {
		font-family: "PT Sans";
	}
	
	main {
	background-color:#282c34;
	color: #f3f3f3;
	font-family:"Roboto";
	min-height: 100vh;
	}

	#total-breaches {
		padding-top: 2rem;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	
</style>