<script>
    import { emailsStore } from '../stores/stores.js'

    let email = ""

    const handleFormSubmit = async () => {
        let addEmail = await fetch(`http://localhost:8000/emails`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({"email":email})
		})
        const data = await addEmail.json()
        emailsStore.update(emails => [...emails, data])
        email = ""
    };

</script>

<div id="form-wrapper">
    <h2>Add new e-mail address</h2>
    
    <form>
        <label for="email">Email Address:</label>
        <input type="text" name="email" bind:value={email}>
        <button on:click|preventDefault={handleFormSubmit}>Add Email</button>
    </form>
</div>

<style>
    h2 {
        margin:0;
        padding-top: 2rem;
    }

    #form-wrapper {
        padding-left: 4rem;
    }
</style>