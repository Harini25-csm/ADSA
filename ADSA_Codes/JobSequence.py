# Job Sequencing with Deadlines - Greedy Strategy

def job_sequencing(jobs):
    """
    Function to schedule jobs to maximize profit.
    Args:
    jobs: List of tuples (JobID, Profit, Deadline)

    Returns:
    Scheduled job order and total profit
    """

    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[1], reverse=True)
    
    # Find maximum deadline
    max_deadline = max(job[2] for job in jobs)
    
    # Initialize slots and result list
    slots = [False] * max_deadline
    job_result = [''] * max_deadline
    total_profit = 0

    # Assign jobs to free slots before their deadline
    for job_id, profit, deadline in jobs:
        for i in range(min(deadline, max_deadline) - 1, -1, -1):
            if not slots[i]:  # Find available slot
                slots[i] = True
                job_result[i] = job_id
                total_profit += profit
                break

    # Display scheduled jobs
    scheduled_jobs = [j for j in job_result if j != '']
    print("\nScheduled Jobs:", ' '.join(scheduled_jobs))
    print(f"Total Profit: {total_profit}")

def main():
    """Function to take input and execute job sequencing."""
    num_jobs = int(input("Enter number of jobs: "))
    jobs = []

    print("Enter job details (JobID Profit Deadline):")
    for _ in range(num_jobs):
        job_id, profit, deadline = input().split()
        jobs.append((job_id, int(profit), int(deadline)))

    job_sequencing(jobs)

if __name__ == "__main__":
    main()
