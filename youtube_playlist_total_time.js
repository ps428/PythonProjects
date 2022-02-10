//just paste this code in the console and get the total play time of any playlist on youtube
times = document.getElementsByClassName('style-scope ytd-thumbnail-overlay-time-status-renderer');

total_time = 0;

for(i=1;i<times.length;i+=2)
{
	curr_time = times[i].innerText.trim();
	curr_time_list = curr_time.split(':');
	
	if(curr_time_list.length < 2)
	{
		// Add 0 minute 
		curr_time_list = [0].concat(curr_time_list);
	}

	if(curr_time_list.length < 3)
	{
		// Add 0 hour 
		curr_time_list = [0].concat(curr_time_list);
	}

	curr_seconds = curr_time_list[0]*60*60 + curr_time_list[1]*60 + curr_time_list[2]*1;
	total_time += curr_seconds;
}

total_hours = 0

if(total_time>=3600)
{
	total_hours = Math.floor(total_time / 3600);
	total_time %= 3600;
}

total_minutes = 0

if(total_time>60)
	total_minutes = Math.floor(total_time / 60);

total_seconds = total_time % 60;

console.log(total_hours,":",total_minutes,":",total_seconds);
