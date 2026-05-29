import { ref, computed } from 'vue'

interface UseFetchOptions<T> {
  initialData?: T
  transform?: (data: T) => T
  onError?: (error: Error) => void
}

export const useFetch = <T>(
  fetcher: () => Promise<{ data: T }>,
  options: UseFetchOptions<T> = {}
) => {
  const { initialData, transform, onError } = options

  const data = ref<T | null>(initialData || null)
  const error = ref<Error | null>(null)
  const loading = ref(false)

  const isEmpty = computed(() => !data.value)

  const execute = async () => {
    loading.value = true
    error.value = null

    try {
      const response = await fetcher()
      data.value = transform ? transform(response.data) : response.data
    } catch (err) {
      error.value = err instanceof Error ? err : new Error(String(err))
      onError?.(error.value)
    } finally {
      loading.value = false
    }
  }

  const reset = () => {
    data.value = initialData || null
    error.value = null
    loading.value = false
  }

  return {
    data,
    error,
    loading,
    isEmpty,
    execute,
    reset
  }
}
