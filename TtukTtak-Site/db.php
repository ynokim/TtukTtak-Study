<?php

    header('Content-Type: text/html; charset=utf-8');

    $db = new mysqli("localhost", "root", "12qwaszx", "TtukTtak");
    $db -> set_charset("utf8");

    function mq($query){
        global $db;
        return $db -> query($query);
    }
    
    
    /*if($db -> connect_error) {
        echo 'ERROR NO: '.$db -> connect_errno;
        echo '<br>';
        echo 'ERROR: '.$db -> connect_error;
        exit();
    } else{
        echo 'DB연결이 완료되었습니다.';
        echo '<br>';
        echo 'HOST INFORMATION: '.$db -> host_info;
        echo '<br>';
        echo 'PROTOCOL VERSION: '.$db -> protocol_version;
    }*/

?>