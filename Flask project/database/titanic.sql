-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 18, 2023 at 01:17 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `titanic`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `book_no` int(255) NOT NULL,
  `book_name` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `quantity` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`book_no`, `book_name`, `author`, `quantity`) VALUES
(1, 'ps', 'kalki', 0),
(5, 'PONNIYIN SELVAN', 'KALKI', 2),
(67, 'STRANGER THINGS', 'ELEVEN', 4),
(898, 'ROMEO AND JULIET', 'WILLIAM SHAKSPEARE', 6),
(990, 'PEAKY BLINDERS', 'CILLIAN MURPHY', 3);

-- --------------------------------------------------------

--
-- Table structure for table `issue_books`
--

CREATE TABLE `issue_books` (
  `issue_id` int(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `bookname` varchar(255) NOT NULL,
  `issuedate` date NOT NULL,
  `expdate` date NOT NULL,
  `retundate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `issue_books`
--

INSERT INTO `issue_books` (`issue_id`, `username`, `bookname`, `issuedate`, `expdate`, `retundate`) VALUES
(1, 'hari', 'ps-1', '2023-06-28', '2023-07-18', '2023-07-14'),
(32, 'Naveen', 'philosophy', '2023-06-28', '2023-07-13', '2023-06-28'),
(1348, 'HARI', 'ENCYCLOPEDIA', '2023-07-04', '2023-07-21', '2023-07-28');

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `tid` int(255) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `bookname` varchar(255) NOT NULL,
  `due` int(255) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`tid`, `user_name`, `bookname`, `due`, `status`) VALUES
(10, 'naveen', 'encyclopedia', 400, 'Paid'),
(11, 'gokul', 'philosophy', 400, 'not paid'),
(12, 'hari', 'enc', 120, 'paid'),
(14, 'praveen', 'teacher', 1234, 'not paid'),
(786, 'SARAVANA', 'JULIUS CEASER', 2000, 'UNPAID'),
(889, 'PREMNATH', 'ROMEO AND JULIET', 600, 'UNPAID');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(255) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `user_name`, `Email`, `Password`) VALUES
(1, 'praveen', 'praveenpopz@gmail.com', '2028'),
(2, 'naveen', 'naveen@gmail.com', '2721'),
(7, 'RITHIK', 'rithik@gmail.com', '0876'),
(8, 'harikrish', 'hari@gmail.com', '9876'),
(9, 'maithesh', 'maithesh@gmail.com', '0987'),
(13, 'Hari', 'harikrish@gmail.com', '9865');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`book_no`,`book_name`);

--
-- Indexes for table `issue_books`
--
ALTER TABLE `issue_books`
  ADD PRIMARY KEY (`issue_id`);

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`tid`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`,`user_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `book_no` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=991;

--
-- AUTO_INCREMENT for table `issue_books`
--
ALTER TABLE `issue_books`
  MODIFY `issue_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1569;

--
-- AUTO_INCREMENT for table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `tid` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=890;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
