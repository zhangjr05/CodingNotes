class NDMatrix:
    """N维矩阵类"""
    
    def __init__(self, data):
        self.data = []
        self.shape = self._get_shape(data)
        self._flatten_data(data)
        self.strides = self._compute_strides(self.shape)
        self.offset = 0
    

    def _compute_strides(self, shape):
        strides = [1]
        for dim in reversed(shape[1:]):
            strides.insert(0, strides[0] * dim)
        return tuple(strides)
    

    def _get_shape(self, data):
        shape = []
        current = data
        while isinstance(current, list):
            shape.append(len(current))
            if not current:
                break
            current = current[0]
        self._validate_data(data, shape)
        return tuple(shape)
    

    def _validate_data(self, data, shape, depth=0):
        if depth >= len(shape):
            return
        if not isinstance(data, list):
            raise ValueError
        if len(data) != shape[depth]:
            raise ValueError
        for item in data:
            self._validate_data(item, shape, depth + 1)


    def _flatten_data(self, data):
        if not isinstance(data, list):
            self.data.append(data)
            return
        for item in data:
            self._flatten_data(item)
    

    def _calculate_index(self, indices):
        if len(indices) != len(self.shape):
            raise IndexError
        idx = self.offset
        for i, (ind, stride) in enumerate(zip(indices, self.strides)):
            if ind < 0 or ind >= self.shape[i]:
                raise IndexError
            idx += ind * stride
        return idx
    

    def __getitem__(self, indices):
        if not isinstance(indices, tuple):
            indices = (indices,)
        return self.data[self._calculate_index(indices)]


    def __setitem__(self, indices, value):
        if not isinstance(indices, tuple):
            indices = (indices,)
        self.data[self._calculate_index(indices)] = value


    def transpose(self, axes=None):
        if axes is None:
            axes = tuple(range(len(self.shape) - 1, -1, -1))
        if len(axes) != len(self.shape):
            raise ValueError
        result = NDMatrix([0])
        result.shape = tuple(self.shape[axis] for axis in axes)
        result.strides = tuple(self.strides[axis] for axis in axes)
        result.data = self.data
        result.offset = self.offset
        return result
    

    def reshape(self, new_shape):
        if self.size() != self._calculate_size(new_shape):
            raise ValueError
        result = NDMatrix([0])
        result.shape = new_shape
        result.data = self.data.copy()
        return result
    

    def size(self):
        return self._calculate_size(self.shape)
    

    def _calculate_size(self, shape):
        if not shape:
            return 0
        size = 1
        for dim in shape:
            size *= dim
        return size
