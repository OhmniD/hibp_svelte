<script>
    export let emails
    import HibpData from './HipbData.svelte'
</script>

<div>
		{#each emails as {email, num_of_breaches, id}}
		<p>{email} - {num_of_breaches} (id {id})</p>
		<HibpData email={email}/>
		{:else}
		<p>Nothing to see here yet</p>
		{/each}
	</div>