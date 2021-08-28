

class Djkistra
  def initialize(graph, start_node)
    @graph = graph
    @start_node = start_node
    @distances = {}
    @previous = {}
    @queue = []
  end

  def shortest_path
    @distances[@start_node] = 0
    @queue.push(@start_node)

    while @queue.length > 0
      current_node = @queue.shift
      @graph.neighbors(current_node).each do |neighbor|
        if @distances[neighbor] == nil
          @distances[neighbor] = @distances[current_node] + @graph.distance(current_node, neighbor)
          @previous[neighbor] = current_node
          @queue.push(neighbor)
        end
      end
    end
    @distances
  end

  def shortest_path_to(node)
    path = []
    while node != @start_node
      path.push(node)
      node = @previous[node]
    end
    path.push(@start_node)
    path.reverse
  end
end