document.addEventListener('DOMContentLoaded', function() {
    // Elements for the diagnosis form
    const diagnoseBtn = document.getElementById('diagnose-btn');
    const issueDescription = document.getElementById('issue-description');
    const loadingElement = document.getElementById('loading');
    const diagnosisResult = document.getElementById('diagnosis-result');
    const diagnosisContent = document.getElementById('diagnosis-content');
    const resolutionNotes = document.getElementById('resolution-notes');
    const markResolvedBtn = document.getElementById('mark-resolved');
    
    // Elements for the history page
    const filterButtons = document.querySelectorAll('.filter-btn');
    const issueCards = document.querySelectorAll('.issue-card');
    
    // Current issue ID (set after diagnosis)
    let currentIssueId = null;
    
    // Handle diagnosis button click
    if (diagnoseBtn) {
        diagnoseBtn.addEventListener('click', async function() {
            const description = issueDescription.value.trim();
            
            if (!description) {
                alert('Please describe your issue first.');
                return;
            }
            
            // Show loading indicator
            diagnoseBtn.disabled = true;
            loadingElement.classList.remove('hidden');
            diagnosisResult.classList.add('hidden');
            
            try {
                const response = await fetch('/api/diagnose', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ issue: description })
                });
                
                if (!response.ok) {
                    throw new Error('Failed to get diagnosis');
                }
                
                const data = await response.json();
                
                // Display the diagnosis
                diagnosisContent.innerHTML = formatDiagnosis(data.diagnosis);
                currentIssueId = data.id;
                
                // Show the diagnosis section
                diagnosisResult.classList.remove('hidden');
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while getting the diagnosis. Please try again.');
            } finally {
                // Hide loading indicator
                loadingElement.classList.add('hidden');
                diagnoseBtn.disabled = false;
            }
        });
    }
    
    // Handle mark as resolved button click
    if (markResolvedBtn) {
        markResolvedBtn.addEventListener('click', async function() {
            if (!currentIssueId) {
                alert('No active issue to resolve.');
                return;
            }
            
            const resolution = resolutionNotes.value.trim();
            
            if (!resolution) {
                alert('Please add some notes about how you resolved the issue.');
                return;
            }
            
            try {
                const response = await fetch('/api/resolve', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        id: currentIssueId,
                        resolution: resolution
                    })
                });
                
                if (!response.ok) {
                    throw new Error('Failed to mark issue as resolved');
                }
                
                alert('Issue marked as resolved! Thank you for your feedback.');
                
                // Reset the form
                issueDescription.value = '';
                resolutionNotes.value = '';
                diagnosisResult.classList.add('hidden');
                currentIssueId = null;
                
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while resolving the issue. Please try again.');
            }
        });
    }
    
    // Handle filter buttons on history page
    if (filterButtons.length > 0) {
        filterButtons.forEach(button => {
            button.addEventListener('click', function() {
                // Update active button
                filterButtons.forEach(btn => btn.classList.remove('active'));
                this.classList.add('active');
                
                const filter = this.dataset.filter;
                
                // Filter the issue cards
                issueCards.forEach(card => {
                    if (filter === 'all') {
                        card.style.display = 'block';
                    } else if (filter === 'resolved' && card.classList.contains('resolved')) {
                        card.style.display = 'block';
                    } else if (filter === 'unresolved' && card.classList.contains('unresolved')) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }
    
    // Helper function to format the diagnosis text
    function formatDiagnosis(text) {
        // Replace section headers with styled headers
        text = text.replace(/DIAGNOSIS:/g, '<strong class="section-header">DIAGNOSIS:</strong>');
        text = text.replace(/SOLUTION:/g, '<strong class="section-header">SOLUTION:</strong>');
        text = text.replace(/PREVENTION:/g, '<strong class="section-header">PREVENTION:</strong>');
        
        // Convert line breaks to HTML
        text = text.replace(/\n/g, '<br>');
        
        return text;
    }
}); 