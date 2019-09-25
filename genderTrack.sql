BEGIN TRANSACTION
--
-- Create model Activity
--
CREATE TABLE [genderTrack_activity] ([id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, [outcome] nvarchar(8) NOT NULL, [total_budget] double precision NOT NULL, [activity] nvarchar(500) NOT NULL, [sub_activity] nvarchar(500) NOT NULL, [cost] double precision NOT NULL, [description] nvarchar(max) NOT NULL);
COMMIT;
