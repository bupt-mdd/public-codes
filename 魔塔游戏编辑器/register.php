<?php
//setcookie("user", "Alex Porter", time()+3600);
$dbc = mysqli_connect('qdm107936287.my3w.com', 'qdm107936287', 'mnhg1234', 'qdm107936287_db')
or die('Error connecting to MySQL server.');
$username = mysqli_real_escape_string($dbc, trim( $_REQUEST['usernamesignup']));
$password1 = mysqli_real_escape_string($dbc, trim( $_REQUEST['passwordsignup']));
$password2 = mysqli_real_escape_string($dbc, trim( $_REQUEST['passwordsignup_confirm']));
$email =mysqli_real_escape_string($dbc, trim( $_REQUEST['emailsignup']));
if (!empty($username) && !empty($password1) && !empty($password2) && ($password1 == $password2)) {
    // Make sure someone isn't already registered using this username
    $query = "SELECT * FROM customer_inf WHERE name = '$username'";
    $data = mysqli_query($dbc, $query);
    if (mysqli_num_rows($data) == 0) {
        // The username is unique, so insert the data into the database
       // $query = "INSERT INTO mismatch_user (username, password, join_date) VALUES ('$username', SHA1('$password1'), NOW())";
        $sha=sha1($password1);
        $query = "INSERT INTO customer_inf(name,password,email) " .
            "VALUES ('$username', '$sha','$email')";
        mysqli_query($dbc, $query);

        // Confirm success with the user
        echo '<p>Your new account has been successfully created. You\'re now ready to <a href="index.php">log in</a>.</p>';
        mysqli_close($dbc);
        exit();
    }
    else {
        // An account already exists for this username, so display an error message
        echo '<p class="error">An account already exists for this username. Please use a different address.</p>';
        $username = "";
    }
}
else {
    echo '<p class="error">You must enter all of the sign-up data, including the desired password twice.</p>';
}
?>
