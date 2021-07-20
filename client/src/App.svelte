<script>
import { onMount } from 'svelte';
import Modal from 'svelte-simple-modal';

	import Emails from './components/Email.svelte'
	import Form from './components/Form.svelte'

	let emails = [];
	let total_breaches = 0

	async function getEmails() {
		let response = await fetch('http://localhost:8000/emails');

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}
		emails = await response.json()

		emails.map(email => total_breaches += email.num_of_breaches)
	}



	onMount(() => {
		getEmails()
	})
	
</script>

<main>
	<Form />
	<h3>Total breaches: {total_breaches}</h3>
	<Modal>
		<Emails emails={emails}/>
	</Modal>
	

</main>

<style>
	@import url('https://fonts.googleapis.com/css2?family=PT+Sans&family=Roboto&display=swap');

	* {
		margin: 0;
		padding: 0;
	}
	
	main {
	background-color:#282c34;
	color: #f3f3f3;
	font-family:"Roboto";
	min-height: 100vh;
	}
	
</style>