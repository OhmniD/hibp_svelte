<script>
    export let emails
    import HibpData from './HipbData.svelte'
</script>

<section>
	<ul>
		{#each emails as {email, num_of_breaches, id}}
		<li class="email-list-item">
		<p>{email} - {num_of_breaches} breaches</p>
		<HibpData email={email}/>
		</li>
		{:else}
		<p>Nothing to see here yet</p>
		{/each}
	</ul>
	
</section>

<style>
	.email-list-item {
		border: solid 1px black;
		list-style-type: none;
		margin: 1rem;
	}
</style>