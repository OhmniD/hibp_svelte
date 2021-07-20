<script>
    export let emails
    import HibpData from './HipbData.svelte'
</script>

<section>
	<ul class="email-list">
		{#each emails as email}
		<li class="email-list-item">
		<h3>{email.email}</h3>
		<p>{email.num_of_breaches} breaches</p>
		<HibpData email={email}/>
		<a href="http://localhost:8000/emails/{email.id}/delete"><button>Delete</button></a>
		</li>
		{:else}
		<p>Loading...</p>
		{/each}
	</ul>
	
</section>

<style>
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
</style>