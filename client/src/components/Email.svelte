<script>
    export let emails
	import { element, prevent_default } from 'svelte/internal'
    import HibpData from './HipbData.svelte'
	import { emailsStore, totalBreachesStore } from '../stores/stores.js'
	import { fade } from 'svelte/transition'

	const handleDeleteClick = async (email) => {
			// emails.forEach(element, i => {
			// 	if (element.id === email.id) {
			// 		console.log(element.id)
			// 		console.log(email.id)
			// 		emails.splice(i, 1);
			// 	}
				
			// });

			for (let i = 0; i < emails.length; i++) {
				if (emails[i].id === email.id) {
					emails.splice(i, 1)
				}
			}

			totalBreachesStore.update(n => n - email.num_of_breaches);

			emailsStore.set([...emails])

		let deleteEmail = await fetch(`http://localhost:8000/emails/${email.id}/delete`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		})

		

		
	}
</script>

<section>
	<ul class="email-list">
		{#each emails as email}
		<li transition:fade class="email-list-item">
		<div class="email-and-delete">
			<h3>{email.email}</h3>
			<p class="delete-icon" on:click|preventDefault={handleDeleteClick(email)}>✖️</p>
		</div>
		<p class="num_of_breaches">{email.num_of_breaches} breaches</p>
		<HibpData email={email}/>
		
		</li>
		{:else}
		<p>Add an e-mail address to get started.</p>
		{/each}
	</ul>
	
</section>

<style>
	h3 {
		font-family: "PT Sans";
	}

	p {
		font-family: "Signika";
	}

	.email-list {
	list-style-type: none;
	display:grid;
	grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
	flex-wrap: wrap;
	margin: 1rem;
	grid-gap: 1rem;
	}

	.email-list-item {
	color: #f3f3f3;
	list-style-type: none;
	height: 250px;
	width: 400px;
	min-width: 150px;
	padding: 1.5rem;
	border-radius: 16px;
	background-color: #1d1f24;
	box-shadow: -1rem 2rem 3rem #000;
	transition: 0.2s;
	}

	.email-and-delete {
		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.num_of_breaches {
		text-align: center;
	}

	.delete-icon {
    transition: 0.15s ease-in-out;
	padding-right: 1rem;
	}
	.delete-icon:hover {
    transform: scale(1.3);
    transition: 0.15s ease-in-out;
    cursor: pointer;
	}
</style>