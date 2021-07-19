<div id="form-wrapper">
    <h2>Add new e-mail address</h2>
    
    <form action="http://localhost:8000/emails" method="POST">
        <label for="email">Email Address:</label>
        <input type="text" name="email">
        <input type="submit" value="Add Email">
    
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