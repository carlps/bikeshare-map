--View to show latest station information
CREATE VIEW public.latest_station_info AS
SELECT 
	latest.station_id
	,station.station_name
	,station.lon
	,station.lat
	,status.num_bikes_available
	,status.num_docks_available
	,latest.last_updated
FROM public.station_status status
INNER JOIN (
	SELECT 
		MAX(last_updated) AS last_updated
		,station_id
	FROM public.station_status
	GROUP BY station_id
) latest
ON status.last_updated = latest.last_updated
AND status.station_id = latest.station_id
INNER JOIN public.station_information station
ON status.station_id = station.station_id;

-- update [user] with your username
GRANT SELECT ON public.latest_station_info TO [user];