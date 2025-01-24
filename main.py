import pygame
import random
import sys

pygame.init()

bars = 100

width, height = 1080, 720
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
offset_x = 40
offset_y = 20
fps = bars * 2.4
clock = pygame.time.Clock()

colors = {
  'black': (20, 20, 20),
  'white': (230, 230, 230),
  'gray': (50, 50, 50),
  'pink': (247, 140, 255),
  'orange': (255, 200, 140),
  'red': (255, 0, 84),
}

font = pygame.font.Font('OpenSans.ttf', 30)
def draw_things(arr, bar_width, height_mult, current_bar=None):
  global paused
  screen.fill(colors['black'])

  draw_bars(arr, bar_width, height_mult, current_bar)

  if paused:
    pause_text = font.render("Paused - Space to unpause", True, colors['orange'])
    screen.blit(pause_text, ((width - pause_text.get_width()) // 2, 10))
  algorithm_text = font.render(algorithm, True, colors['pink'])
  screen.blit(algorithm_text, (10, 10))

  pygame.display.flip()
  clock.tick(fps)

# Sorts 
# - Insertion
def insertion_sort(arr, bar_width, height_mult):
  global paused
  for i in range(1, len(arr)):
    if paused:
      return arr
    curr = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > curr:
      arr = process_inputs(arr)
      if paused:
        return arr
      arr[j + 1] = arr[j]
      j -= 1
      draw_things(arr, bar_width, height_mult, j)
    
    arr[j + 1] = curr

  paused = True
  return arr

# - Selection
def selection_sort(arr, bar_width, height_mult):
  global paused
  n = len(arr)
  for i in range(n):
    if paused: return arr
    min_idx = i
    for j in range(i + 1, n):
      arr = process_inputs(arr)
      if paused: return arr
      if arr[j] < arr[min_idx]:
        min_idx = j
      draw_things(arr, bar_width, height_mult, j)
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  
  paused = True
  return arr

# - Bubble
def bubble_sort(arr, bar_width, height_mult):
  global paused
  n = len(arr)
  
  for i in range(n):
    if paused:
      return arr
    sorted = True
    
    for j in range(n - i - 1):
      arr = process_inputs(arr)
      if paused:
        return arr
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        sorted = False
      draw_things(arr, bar_width, height_mult, j)
    
    if sorted:
      break
  
  paused = True
  return arr

# - Shaker
def shaker_sort(arr, bar_width, height_mult):
  global paused
  n = len(arr)
  swapped = True
  start = 0
  end = n - 1

  while swapped and not paused:
    swapped = False
    for i in range(start, end):
      arr = process_inputs(arr)
      if paused:
        return arr
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        swapped = True
      draw_things(arr, bar_width, height_mult, i)
    
    if not swapped:
      break

    swapped = False
    end -= 1

    for i in range(end - 1, start - 1, -1):
      arr = process_inputs(arr)
      if paused:
        return arr
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        swapped = True
      draw_things(arr, bar_width, height_mult, i)
    
    start += 1

  paused = True
  return arr

# - Quick
def quick_sort(arr, bar_width, height_mult):
  global paused
  def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
      arr = process_inputs(arr)
      if paused:
        return -1
      if arr[j] < pivot:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
      draw_things(arr, bar_width, height_mult, j)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

  def quick_sort_recursive(arr, low, high):
    if low < high:
      pi = partition(arr, low, high)
      if pi == -1:
        return
      quick_sort_recursive(arr, low, pi - 1)
      quick_sort_recursive(arr, pi + 1, high)

  quick_sort_recursive(arr, 0, len(arr) - 1)

  paused = True
  return arr

# - Heap
def heapify(arr, n, i):
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2

  if left < n and arr[left] > arr[largest]:
    largest = left

  if right < n and arr[right] > arr[largest]:
    largest = right

  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    draw_things(arr, bar_width, height_mult, i)
    heapify(arr, n, largest)

def heap_sort(arr, bar_width, height_mult):
  global paused
  n = len(arr)

  for i in range(n // 2 - 1, -1, -1):
    arr = process_inputs(arr)
    if paused:
      return arr
    heapify(arr, n, i)

  for i in range(n - 1, 0, -1):
    arr = process_inputs(arr)
    if paused:
      return arr
    arr[i], arr[0] = arr[0], arr[i]
    draw_things(arr, bar_width, height_mult, i)
    heapify(arr, i, 0)

  paused = True
  return arr

# - Odd/Even sort
def odd_even_sort(arr, bar_width, height_mult):
  global paused
  n = len(arr)
  sorted = False

  while not sorted and not paused:
    sorted = True
    for i in range(1, n - 1, 2):
      arr = process_inputs(arr)
      if paused:
        return arr
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        sorted = False
      draw_things(arr, bar_width, height_mult, i)

    for i in range(0, n - 1, 2):
      arr = process_inputs(arr)
      if paused:
        return arr
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        sorted = False
      draw_things(arr, bar_width, height_mult, i)

  paused = True
  return arr

# Radix
def radix_sort(arr, bar_width, height_mult):
  global paused
  max_val = max(arr)
  exp = 1

  while max_val // exp > 0 and not paused:
    count = [0] * 10
    output = [0] * len(arr)

    for i in range(len(arr)):
      arr = process_inputs(arr)
      if paused:
        return arr
      index = arr[i] // exp
      count[index % 10] += 1

    for i in range(1, 10):
      count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
      arr = process_inputs(arr)
      if paused:
        return arr
      index = arr[i] // exp
      output[count[index % 10] - 1] = arr[i]
      count[index % 10] -= 1

    for i in range(len(arr)):
      arr[i] = output[i]
      draw_things(arr, bar_width, height_mult, i)

    exp *= 10

  paused = True
  return arr

# Modified bogo
def mod_bogo_sort(arr, bar_width, height_mult):
  global paused
  sorted_arr = sorted(arr)

  while arr != sorted_arr and not paused:
    arr = process_inputs(arr)
    if paused:
      return arr

    temp_arr = [arr[i] for i in range(len(arr)) if arr[i] != sorted_arr[i]]
    random.shuffle(temp_arr)

    j = 0
    for i in range(len(arr)):
      if arr[i] != sorted_arr[i]:
        arr[i] = temp_arr[j]
        j += 1

    draw_things(arr, bar_width, height_mult)

  paused = True
  return arr

# - Regular Bogo
def bogo_sort(arr, bar_width, height_mult):
  global paused
  def is_sorted(arr):
    for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
        return False
    return True
  
  while not is_sorted(arr) and not paused:
    arr = process_inputs(arr)
    if paused:
      return arr
    random.shuffle(arr)
    draw_things(arr, bar_width, height_mult)

  paused = True

# - Bozo
def bozo_sort(arr, bar_width, height_mult):
  global paused
  def is_sorted(arr):
    for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
        return False
    return True

  while not is_sorted(arr) and not paused:
    arr = process_inputs(arr)
    if paused:
      return arr
    i, j = random.randint(0, len(arr) - 1), random.randint(0, len(arr) - 1)
    arr[i], arr[j] = arr[j], arr[i]
    draw_things(arr, bar_width, height_mult, i)
  
  paused = True
  return arr

# - Stalin
def stalin_sort(arr, bar_width, height_mult):
  global paused
  i = 1
  while i < len(arr):
    draw_things(arr, bar_width, height_mult, i)
    if arr[i] < arr[i-1]:
      arr.pop(i)
    else:
      i += 1
  
  paused = True
  return arr

# - Miracle
def miracle_sort(arr, bar_width, height_mult):
  global paused
  def is_sorted(arr):
    for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
        return False
    return True

  while not (paused or is_sorted(arr)):
    arr = process_inputs(arr)
    draw_things(arr, bar_width, height_mult)
    pass

  paused = True
  return arr

# - Intelligent design
def intelligent_design_sort(arr, bar_width, height_mult):
  global paused
  arr = process_inputs(arr)

  paused = True
  return arr

# !!
algorithms = {
  'insertion': insertion_sort,
  'selection': selection_sort,
  'bubble': bubble_sort,
  'shaker': shaker_sort,
  'quick': quick_sort,
  'heap': heap_sort,
  'odd/even': odd_even_sort,
  'radix': radix_sort,
  'bogo': bogo_sort,
  'modified bogo': mod_bogo_sort,
  'bozo': bozo_sort,
  'stalin': stalin_sort,
  'miracle': miracle_sort,
  'intel. des.': intelligent_design_sort,
}
def cycle(list):
  while True: yield from list
algorithm_cycler = cycle(list(algorithms.keys()))
algorithm = next(algorithm_cycler)

def sort(arr):
  while paused:
    draw_things(arr, bar_width, height_mult)
    arr = process_inputs(arr)

  return algorithms[algorithm](arr, bar_width, height_mult)

def draw_bars(arr, bar_width, height_mult, current_bar=None):
  for idx, i in enumerate(arr):
    color = colors['red'] if idx == current_bar else colors['white']
    pygame.draw.rect(screen, color, (bar_width * idx + offset_x, height - i * height_mult - offset_y, bar_width, i * height_mult))

def process_inputs(arr):
  global screen, width, height, offset_x, offset_y, clock, running, bar_width, height_mult, algorithm, paused
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
          arr = [i for i in range(1, bars + 1)]
          random.shuffle(arr)
          paused = True
          arr = sort(arr)
        elif event.key == pygame.K_e:
          paused = True
          clock.tick(fps)
          arr = [i for i in range(1, bars + 1)]
          random.shuffle(arr)
          algorithm = next(algorithm_cycler)
        elif event.key == pygame.K_SPACE:
          paused = not paused
      elif event.type == pygame.VIDEORESIZE:
        width, height = event.size
        offset_x = (width - len(arr) * bar_width) // 2
        offset_y = 1/30*height
        bar_width = (width - 2 * offset_x) // len(arr)
        height_mult = (height - 2 * offset_y) / max(arr)
        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
  return arr


running = False
paused = True
def main():
  global screen, width, height, offset_x, offset_y, clock, running, bar_width, height_mult, paused

  arr = [i for i in range(1, bars + 1)]
  random.shuffle(arr)

  bar_width = (width - 2 * offset_x) // len(arr)
  height_mult = (height - 2 * offset_y) / max(arr)
  offset_x = (width - len(arr) * bar_width) // 2
  offset_y = (height - max(arr) * height_mult) // 2

  running = True
  while running:
    if paused:
      arr = process_inputs(arr)
    else:
      sort(arr)

    draw_things(arr, bar_width, height_mult)
    pygame.display.flip()
    clock.tick(fps)

if __name__ == "__main__":
  main()
  pygame.quit()