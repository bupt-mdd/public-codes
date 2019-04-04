<?php
@session_start();
$error_msg = "";
if (!isset($_SESSION['user_id'])) {
    $dbc = mysqli_connect('qdm107936287.my3w.com', 'qdm107936287', 'mnhg1234', 'qdm107936287_db')
    or die('Error connecting to MySQL server.');
    $user_username = mysqli_real_escape_string($dbc, trim($_REQUEST['username']));
    $user_password = mysqli_real_escape_string($dbc, trim($_REQUEST['password']));
if (!empty($user_username) && !empty($user_password)) {
    $query = "SELECT id, name FROM customer_inf WHERE name = '$user_username' AND password = sha1('$user_password')";
    $data = mysqli_query($dbc, $query);
    if (mysqli_num_rows($data) == 1) {
        $row = mysqli_fetch_array($data);
        $_SESSION['id'] = $row['id'];
        $_SESSION['name'] = $row['name'];
        setcookie('id', $row['id'], time() + (60 * 60 * 24 * 30));    // expires in 30 days
        setcookie('name', $row['name'], time() + (60 * 60 * 24 * 30));  // expires in 30 days
        @header('Location:show.php');
    }
    else {
        // The username/password are incorrect so set an error message
        @header('Location:index.php');
    }

}
else {
    // The username/password weren't entered so set an error message
     @header('Location:index.php');
}
}
?>











