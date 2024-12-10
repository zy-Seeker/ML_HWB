import time

# Start the timer
start_time = time.time()
epoch_start_time = time.time()

input_upper = np.load(os.path.join(input_data_dir, f'input_upper_seven_day.npy'))
input_surface = np.load(os.path.join(input_data_dir, f'input_surface_seven_day.npy'))

input_upper = input_upper.astype(np.float32)
input_surface = input_surface.astype(np.float32)

for step in range(1, 8):  # 7 iterations
    # Run the model
    output_upper, output_surface = ort_session_24.run(None, {'input': input_upper,
                                                             'input_surface': input_surface})

    # Update the input for the next iteration
    input_upper, input_surface = output_upper, output_surface

    # Save the output of each timestep
    np.save(os.path.join(output_data_dir, f'output_upper_case_{case_forecast}_step_{step}.npy'), output_upper)
    np.save(os.path.join(output_data_dir, f'output_surface_step_{step}.npy'), output_surface)

epoch_end_time = time.time()

# Calculate the execution time
execution_time = epoch_end_time - epoch_start_time
print(f"Execution time: {execution_time:.5f} seconds")

start_time = time.time()
