async function fetchMetrics() {
	try {
		const response = await fetch(metricsUrl);
		if (!response.ok) {
			throw new Error('Network response was not ok');
		}
		return await response.json();
	} catch (error) {
		console.error('Error fetching metrics:', error);
		return null;
	}
}

function updateCPUUsage(cpuUsage) {
	document.getElementById('total-cpu-usage').innerText = `${cpuUsage.toFixed(2)}%`;
}

function updateCPUUsageByCore(cpuUsageByCore) {
	const coresContainer = document.getElementById('cores-container');
	coresContainer.innerHTML = ''; // Clear previous cores

	const fragment = document.createDocumentFragment();
	Object.keys(cpuUsageByCore).forEach((core, index) => {
		const coreUsage = cpuUsageByCore[core].toFixed(2);
		const coreElement = document.createElement('div');
		coreElement.innerHTML = `
      <div class="text-sm text-muted-foreground">Core ${index + 1}</div>
      <div class="font-bold text-primary">${coreUsage}%</div>
    `;
		fragment.appendChild(coreElement);
	});
	coresContainer.appendChild(fragment);
}

function updateMemoryInfo(memoryInfo) {
	const { total, free, available, percent } = memoryInfo;
	const totalMemory = (total / (1024 ** 3)).toFixed(2);
	const freeMemory = (free / (1024 ** 3)).toFixed(2);
	const availableMemory = (available / (1024 ** 3)).toFixed(2);
	const usedMemoryPercent = percent.toFixed(2);

	document.getElementById('total-memory').innerText = `${totalMemory}GB`;
	document.getElementById('free-memory').innerText = `${freeMemory}GB`;
	document.getElementById('available-memory').innerText = `${availableMemory}GB`;
	document.getElementById('used-memory').innerText = `${usedMemoryPercent}%`;
}

async function updateMetrics() {
	const data = await fetchMetrics();
	if (!data) return;

	// Hide loading indicator and show dashboard content
	document.getElementById('loading').classList.add('hidden');
	document.getElementById('dashboard-content').classList.remove('hidden');

	// Update CPU and Memory Info
	updateCPUUsage(data.cpu_usage);
	updateCPUUsageByCore(data.cpu_usage_by_core);
	updateMemoryInfo(data.memory_info);
}

// Initial call to update metrics
updateMetrics();

// Update metrics every 2 seconds
setInterval(updateMetrics, 2000);
