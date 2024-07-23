CREATE TABLE playlist (
track_id int(11) NOT NULL,
track_artist varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
track_bpm float DEFAULT NULL,
track_device varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
track_genre varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
track_key varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
track_label varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
track_title varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
track_timestamp timestamp NOT NULL,
rekordbox_id int(11) NOT NULL
)
