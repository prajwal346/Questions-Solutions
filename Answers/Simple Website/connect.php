<?php
$name= $_POST['name'];
$clientemail= $_POST['clientemail'];
$clientphone=$_POST['clientphone'];
$enquiry=$_POST['enquiry'];
$checkbox=$_POST['checkbox'];

// connection database...
$conn= new mysqli('localhost','root','','test');
if($conn->connect_error){
    die('connection failed:'.$conn->connect_error);
}
else{
    $stmt = $conn->prepare("insert into registration( name ,clientemail, clientphone, enquiry,checkbox)values( ?, ?, ?, ?)");
    $stmt->bind_param("ssis" $name, $clientemail, $clientphone, $enquiry, $checkbox);
    $stmt->execute();
    echo "Registration Sucessfully !!! Prajwal will contact you within 24Hours!";
    $stmt->close();
    $conn->close();
}

?>