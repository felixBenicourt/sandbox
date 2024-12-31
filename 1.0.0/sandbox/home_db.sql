-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 18, 2024 at 03:08 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `home_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `asset`
--

CREATE TABLE `asset` (
  `id` int(11) NOT NULL,
  `projectId` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `task` varchar(500) DEFAULT NULL,
  `variation` varchar(500) DEFAULT NULL,
  `version` int(11) DEFAULT 1,
  `status` enum('In Progress','Approved','Deprecated') DEFAULT 'In Progress'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `asset`
--

INSERT INTO `asset` (`id`, `projectId`, `name`, `type`, `task`, `variation`, `version`, `status`) VALUES
(1, 1, 'rocketGirl', 'chr', 'rig', 'main', 1, 'Approved'),
(2, 1, 'rocketGirl', 'chr', 'mdl', 'main', 1, 'Approved'),
(3, 1, 'mrButton', 'chr', 'mdl', 'main', 1, 'Approved'),
(4, 1, 'thanos', 'chr', 'mdl', 'main', 1, 'Approved'),
(5, 1, 'thanos', 'chr', 'rig', 'main', 1, 'Approved');

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

CREATE TABLE `project` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`id`, `name`) VALUES
(1, 'template');

-- --------------------------------------------------------

--
-- Table structure for table `sequence`
--

CREATE TABLE `sequence` (
  `id` int(11) UNSIGNED NOT NULL,
  `projectId` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `sequence`
--

INSERT INTO `sequence` (`id`, `projectId`, `name`) VALUES
(1, 1, '00003');

-- --------------------------------------------------------

--
-- Table structure for table `shot`
--

CREATE TABLE `shot` (
  `id` int(11) NOT NULL,
  `projectId` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `task` varchar(255) NOT NULL,
  `variation` varchar(255) NOT NULL,
  `sequenceId` int(11) NOT NULL,
  `version` int(11) NOT NULL,
  `cutIn` int(11) NOT NULL,
  `cutOut` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `shot`
--

INSERT INTO `shot` (`id`, `projectId`, `name`, `type`, `task`, `variation`, `sequenceId`, `version`, `cutIn`, `cutOut`) VALUES
(1, 1, '00000', 'shot', 'ani', 'main', 0, 1, 0, 0),
(2, 1, '00001', 'shot', 'ani', 'main', 0, 1, 0, 0),
(3, 1, '00002', 'shot', 'ani', 'main', 0, 1, 0, 0),
(4, 1, '00003', 'shot', 'ani', 'main', 0, 1, 0, 0),
(5, 1, '00000', 'shot', 'cfx', 'main', 0, 1, 0, 0),
(6, 1, '00001', 'shot', 'cfx', 'main', 0, 1, 0, 0),
(7, 1, '00002', 'shot', 'cfx', 'main', 0, 1, 0, 0),
(8, 1, '00003', 'shot', 'cfx', 'main', 0, 1, 0, 0),
(9, 1, '00000', 'shot', 'brk', 'main', 0, 1, 0, 0),
(10, 1, '00001', 'shot', 'brk', 'main', 0, 1, 0, 0),
(11, 1, '00002', 'shot', 'brk', 'main', 0, 1, 0, 0),
(12, 1, '00003', 'shot', 'brk', 'main', 0, 1, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `asset`
--
ALTER TABLE `asset`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sequence`
--
ALTER TABLE `sequence`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `shot`
--
ALTER TABLE `shot`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `asset`
--
ALTER TABLE `asset`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `project`
--
ALTER TABLE `project`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `sequence`
--
ALTER TABLE `sequence`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `shot`
--
ALTER TABLE `shot`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
